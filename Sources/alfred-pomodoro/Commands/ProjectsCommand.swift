//
//  Projects.swift
//  SwiftCLI
//
//  Created by Paul Traylor on 2020/04/19.
//

import Foundation
import SwiftCLI

class ProjectCommand: Command {
    let name = "projects"

    func execute() throws {
        var items = [AlfredRow]()

        let sema = DispatchSemaphore(value: 0)

        Project.list { result in
            switch result {
            case let .failure(error):
                self.stderr <<< error.localizedDescription
            case let .success(projects):
                projects.forEach { project in
                    items.append(AlfredRow(arg: project.id, title: project.name, icon: nil))
                }
            }
            sema.signal()
        }
        sema.wait()

        stdout <<< AlfredJson(items: Array(items.prefix(10))).json
    }
}
