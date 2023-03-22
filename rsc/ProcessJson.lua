dofile("HeadlessWrapper.lua")

require("CharList")

for i = 1, CharCount
do
    loadBuildFromJSON(CharList[i][1][1], CharList[i][2][1])
	GlobalCache.useFullDPS = true
	for i,group in ipairs(build.skillsTab.socketGroupList) do
		group.includeInFullDPS = true
	end
	build.calcsTab:BuildOutput()
	build:RefreshStatList()
	local xmlText = build:SaveDB("code")
    local file = io.open(i .. "char.xml", "w+")
	if not file then
		print("Error", "Couldn't save the build file:\n"..i.."char.xml".."\nMake sure the save folder exists and is writable.")
		return true
	end
	file:write(xmlText)
	file:close()
end
