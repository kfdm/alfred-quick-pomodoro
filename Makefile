build:
	swift build -Xswiftc "-target" \
    -Xswiftc "x86_64-apple-macosx10.12"

update:
	swift package update
	swift package generate-xcodeproj

lint:
	swiftlint autocorrect Sources

release:
	swift build -c release

run: build
	.build/debug/alfred-pomodoro projects

install: build
	install .build/debug/alfred-pomodoro workflow/pomodoro
