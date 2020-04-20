//
//  StartCommand.swift
//
//  Created by Paul Traylor on 2020/04/19.
//

import Foundation
import SwiftCLI

class StartCommand: SemaphoreCommand, Command {
    let name = "start"

    @Key("-d","--duration",description:"How long of a sprint")
    var duration: Int?

    @Key("-p","--project",description:"Project ID")
    var project: String?

    @CollectedParam var message: [String]

    override func executeSemaphore() throws {
        let pomodoro = Pomodoro(title: message.joined(separator: " "), project: project, minutes: duration)
        pomodoro.submit { result in
            switch result {
            case let .failure(error):
                self.stderr <<< error.localizedDescription
            case let .success(newPomodoro):
                self.stdout <<< "\(newPomodoro)"
            }
            self.sema.signal()
        }
    }
}
