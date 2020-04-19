//
//  Projects.swift
//  SwiftCLI
//
//  Created by Paul Traylor on 2020/04/19.
//

import Foundation
import SwiftCLI

class ProjectCommand: SemaphoreCommand, Command {
    let name = "projects"

    override func executeSemaphore() throws {
        var items = [AlfredRow]()
        Project.list { result in
            switch result {
            case let .failure(error):
                self.stderr <<< error.localizedDescription
            case let .success(projects):
                projects.forEach { project in
                    items.append(AlfredRow(arg: project.id, title: project.name, icon: nil))
                }
                self.stdout <<< AlfredJson(items: Array(items.prefix(10))).json
            }
            self.sema.signal()
        }
    }
}
