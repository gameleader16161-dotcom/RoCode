--!strict
-- Copyright (c) 2026 QFR Studios. MIT License.
-- Optional Studio-only checks: call with the local Geometry module loaded.
-- Creates two unparented Parts, destroys them after the assertions even on failure.
return function(Geometry: any)
	local a, b = Instance.new("Part"), Instance.new("Part")
	local ok, failure = pcall(function()
		local cf, size = Geometry.wallBetween(Vector3.zero, Vector3.new(0, 0, 10), 6, 2)
		assert((size - Vector3.new(2, 6, 10)).Magnitude < 0.0001)
		assert((cf.Position - Vector3.new(0, 3, 5)).Magnitude < 0.0001)
		local left = cf:PointToWorldSpace(Vector3.new(0, 0, -5))
		local right = cf:PointToWorldSpace(Vector3.new(0, 0, 5))
		assert(math.abs(left.Z - right.Z) > 9.999)
		assert(not pcall(Geometry.wallBetween, Vector3.zero, Vector3.zero, 6, 2))
		assert(not pcall(Geometry.wallBetween, Vector3.zero, Vector3.new(0, 1, 10), 6, 2))
		assert((Geometry.tileCenter(2, 1, 2, 1, 8, 8) - Geometry.tileCenter(1, 1, 2, 1, 8, 8)).X == 8)
		a.Size, b.Size = Vector3.new(4, 4, 4), Vector3.new(4, 4, 4)
		a.CFrame, b.CFrame = CFrame.new(), CFrame.new(4, 0, 0)
		assert(Geometry.seamOnAxis(a, b, "X", 0.001).classification == "touch")
		b.CFrame = CFrame.new(4.2, 0, 0)
		assert(Geometry.seamOnAxis(a, b, "X", 0.001).classification == "gap")
		b.CFrame = CFrame.new(3.8, 0, 0)
		assert(Geometry.seamOnAxis(a, b, "X", 0.001).classification == "overlap")
		b.CFrame = CFrame.new(4, 10, 0)
		assert(not Geometry.seamOnAxis(a, b, "X", 0.001).candidate)
		b.CFrame = CFrame.Angles(0, 0.5, 0)
		assert(not pcall(Geometry.seamOnAxis, a, b, "X", 0.001))
	end)
	a:Destroy()
	b:Destroy()
	assert(ok, tostring(failure))
	return "RoCode Geometry checks passed in Studio"
end
