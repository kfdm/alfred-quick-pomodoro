//
//  Settings.swift
//
//  Created by Paul Traylor on 2020/04/20.
//

import Foundation
import KeychainAccess

class Settings {
  static let identifier = "net.kungfudiscomonkey.alfred-pomodoro"
  static let defaults = UserDefaults(suiteName: Settings.identifier)!
  static let keychain = Keychain(accessGroup: Settings.identifier)

  static var username: String {
    get { return Settings.defaults.string(forKey: "username")! }
    set { Settings.defaults.set(newValue, forKey: "username") }
  }

  static var password: String {
    get { return Settings.keychain[Settings.username]! }
    set { try? Settings.keychain.set(newValue, key: Settings.username) }
  }
}
