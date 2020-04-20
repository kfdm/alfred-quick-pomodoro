import SwiftCLI

let cli = CLI(
  name: "alfred-pomodoro", version: "1.0.0", description: "Greeter - a friendly greeter",
  commands: [StartCommand(), LoginCommand(), ProjectCommand()])
cli.parser.parseOptionsAfterCollectedParameter = true
cli.goAndExit()
