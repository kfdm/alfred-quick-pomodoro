build:
	swift build

update:
	swift package update
	swift package generate-xcodeproj

lint:
	swiftlint autocorrect Sources

release:
	swift build -c release

run:
	swift run alfred-pomodoro
