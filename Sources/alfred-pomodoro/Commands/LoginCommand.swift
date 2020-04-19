//
//  Login.swift
//  SwiftCLI
//
//  Created by Paul Traylor on 2020/04/19.
//

import SwiftCLI

class LoginCommand: Command {

    let name = "login"
    let shortDescription = "Login and save"

    @Param var username: String
    @Param var password: String

    func execute() throws {
        stdout <<< "Setting password for \(username)"
        Settings.keychain[username] = password
    }
}
