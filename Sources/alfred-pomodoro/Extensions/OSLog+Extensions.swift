//
//  Log.swift
//  NextPomodoro
//
//  Created by Paul Traylor on 2019/09/04.
//  Copyright © 2019 Paul Traylor. All rights reserved.
//

import Foundation
import os

extension OSLog {
    static let favorites = OSLog.init(subsystem: Settings.identifier, category: "Favorites")
    static let pomodoro = OSLog.init(subsystem: Settings.identifier, category: "Pomodoro")
    static let networking = OSLog(subsystem: Settings.identifier, category: "Networking")
    static let mqtt = OSLog(subsystem: Settings.identifier, category: "MQTT")
    static let view = OSLog(subsystem: Settings.identifier, category: "ViewController")
    static let today = OSLog(subsystem: Settings.identifier, category: "TodayWidget")
}
