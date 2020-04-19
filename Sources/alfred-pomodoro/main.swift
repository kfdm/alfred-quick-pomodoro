import SwiftCLI

let myCli = CLI(name: "alfred-pomodoro", version: "1.0.0", description: "Greeter - a friendly greeter", commands: [ProjectCommand()])
myCli.goAndExit()
