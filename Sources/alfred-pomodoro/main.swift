import SwiftCLI
import KeychainAccess

class Settings {
    static var keychain = Keychain(service: "net.kungfudiscomonkey.alfred-pomodoro")
}

let myCli = CLI(name: "alfred-pomodoro", version: "1.0.0", description: "Greeter - a friendly greeter", commands: [LoginCommand(), ProjectCommand()])
myCli.goAndExit()
