import Foundation
import KeychainAccess
import SwiftCLI

class Settings {
    static let identifier = "net.kungfudiscomonkey.alfred-pomodoro"
    static let defaults = UserDefaults(suiteName: Settings.identifier)!
    static let keychain = Keychain(accessGroup: Settings.identifier)
}

let myCli = CLI(name: "alfred-pomodoro", version: "1.0.0", description: "Greeter - a friendly greeter", commands: [LoginCommand(), ProjectCommand()])
myCli.goAndExit()
