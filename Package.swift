// swift-tools-version:5.2
// The swift-tools-version declares the minimum version of Swift required to build this package.

import PackageDescription

let package = Package(
    name: "alfred-pomodoro",
    dependencies: [
        .package(url: "https://github.com/jakeheis/SwiftCLI", from: "6.0.0"),
        .package(url: "https://github.com/kishikawakatsumi/KeychainAccess", from: "4.1.0")
    ],
    targets: [
        .target(
            name: "alfred-pomodoro",
            dependencies: ["SwiftCLI", "KeychainAccess"])

    ]
)
