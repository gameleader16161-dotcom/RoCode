--!strict
-- RoCode by QFR Studios. Copyright (c) 2026 QFR Studios. MIT License.
-- Read-only candidate report. Does not execute source or certify asset safety.
local SceneAudit = {}

function SceneAudit.inspect(root: Instance, maximumDescendants: number?)
	assert(root ~= game and root ~= workspace, "Choose an explicit map/model root, not the whole DataModel or Workspace")
	local limit = maximumDescendants or 10000
	assert(limit >= 1 and limit <= 100000 and limit % 1 == 0, "Invalid scan limit")
	local report = {
		root = root:GetFullName(), scanned = 0, truncated = false,
		parts = 0, meshes = 0, unanchored = 0, collidable = 0, emitters = 0,
		scripts = {} :: { string }, unanchoredSamples = {} :: { string },
	}
	-- Bounded traversal rather than GetDescendants allocating the entire subtree.
	local stack = { root }
	while #stack > 0 do
		local node = table.remove(stack) :: Instance
		if report.scanned >= limit then report.truncated = true; break end
		report.scanned += 1
		if node:IsA("BasePart") then
			report.parts += 1
			if node:IsA("MeshPart") then report.meshes += 1 end
			if node.CanCollide then report.collidable += 1 end
			if not node.Anchored then
				report.unanchored += 1
				if #report.unanchoredSamples < 20 then
					table.insert(report.unanchoredSamples, node:GetFullName())
				end
			end
		elseif node:IsA("LuaSourceContainer") then
			table.insert(report.scripts, node:GetFullName())
		elseif node:IsA("ParticleEmitter") then
			report.emitters += 1
		end
		for _, child in node:GetChildren() do table.insert(stack, child) end
		if report.scanned % 200 == 0 then task.wait() end
	end
	return report
end

return SceneAudit
