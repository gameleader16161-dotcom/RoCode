--!strict
-- RoCode by QFR Studios. Copyright (c) 2026 QFR Studios. MIT License.
-- Local source module, not an external asset require.
local Geometry = {}

local function finite(n: number): boolean
	return n == n and n > -math.huge and n < math.huge
end

local function validVector(v: Vector3): boolean
	return finite(v.X) and finite(v.Y) and finite(v.Z)
end

-- Returns a horizontal wall transform and size; creates no instances.
-- A and B are centerline endpoints at the same floor elevation.
function Geometry.wallBetween(a: Vector3, b: Vector3, height: number, thickness: number): (CFrame, Vector3)
	assert(validVector(a) and validVector(b), "Wall endpoints must be finite")
	assert(finite(height) and height > 0, "Wall height must be positive and finite")
	assert(finite(thickness) and thickness > 0, "Wall thickness must be positive and finite")
	assert(math.abs(a.Y - b.Y) <= 0.0001, "Use equal base elevations for horizontal wall segments")
	local delta = Vector3.new(b.X - a.X, 0, b.Z - a.Z)
	assert(delta.Magnitude > 0.0001, "Wall endpoints must be distinct")
	local center = Vector3.new((a.X + b.X) / 2, a.Y + height / 2, (a.Z + b.Z) / 2)
	return CFrame.lookAt(center, center + delta.Unit), Vector3.new(thickness, height, delta.Magnitude)
end

-- Cell centers derived from shared extents; adjacent cells have no intended gaps.
-- The caller supplies its own origin CFrame and decides whether to create Parts.
function Geometry.tileCenter(column: number, row: number, columns: number, rows: number,
	cellX: number, cellZ: number): Vector3
	assert(finite(columns) and columns >= 1 and columns % 1 == 0, "Invalid column count")
	assert(finite(rows) and rows >= 1 and rows % 1 == 0, "Invalid row count")
	assert(column >= 1 and column <= columns and column % 1 == 0, "Column outside grid")
	assert(row >= 1 and row <= rows and row % 1 == 0, "Row outside grid")
	assert(finite(cellX) and finite(cellZ) and cellX > 0 and cellZ > 0, "Invalid cell dimensions")
	return Vector3.new((column - (columns + 1) / 2) * cellX, 0, (row - (rows + 1) / 2) * cellZ)
end

local function axisValue(v: Vector3, axis: string): number
	if axis == "X" then return v.X end
	if axis == "Y" then return v.Y end
	return v.Z
end

-- Only same-rotation rectangular Block Parts, using A's local axes.
-- Returns signed face separation, tangential overlap, and gap/touch/overlap.
-- It checks a selected pair, not arbitrary map holes or mesh topology.
function Geometry.seamOnAxis(a: Part, b: Part, axis: string, tolerance: number)
	assert(a.Shape == Enum.PartType.Block and b.Shape == Enum.PartType.Block, "Only Block Parts supported")
	assert(axis == "X" or axis == "Y" or axis == "Z", "Axis must be X, Y or Z")
	assert(finite(tolerance) and tolerance >= 0, "Invalid seam tolerance")
	local relative = a.CFrame:ToObjectSpace(b.CFrame)
	assert((relative.RightVector - Vector3.xAxis).Magnitude < 0.0001
		and (relative.UpVector - Vector3.yAxis).Magnitude < 0.0001,
		"Part rotations must match; rotated-pair diagnosis needs oriented face geometry")
	local offset = relative.Position
	local gap = math.abs(axisValue(offset, axis)) - (axisValue(a.Size, axis) + axisValue(b.Size, axis)) / 2
	local tangentOverlap = true
	for _, tangent in { "X", "Y", "Z" } do
		if tangent ~= axis then
			local overlap = (axisValue(a.Size, tangent) + axisValue(b.Size, tangent)) / 2
				- math.abs(axisValue(offset, tangent))
			if overlap <= tolerance then tangentOverlap = false end
		end
	end
	local classification = if gap > tolerance then "gap" elseif gap < -tolerance then "overlap" else "touch"
	return { separation = gap, tangentialOverlap = tangentOverlap, classification = classification,
		candidate = tangentOverlap }
end

return Geometry
