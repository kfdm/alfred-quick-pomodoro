build:
	swift build

update:
	swift package update
	swift package generate-xcodeproj

format:
	swift-format format -ir Package.swift Sources 

release:
	swift build -c release

run: build
	.build/debug/alfred-pomodoro start  -p 62005a14-3cb9-4b4e-b241-146f04d999e3 --duration 60 test a longer sprint

install: build
	install .build/debug/alfred-pomodoro workflow/pomodoro
