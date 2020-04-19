//
//  Projects.swift
//  SwiftCLI
//
//  Created by Paul Traylor on 2020/04/19.
//

import SwiftCLI

class ProjectCommand: Command {

    let name = "projects"
    let shortDescription = "Says hello to the world"

    func execute() throws {
        stdout <<< "Hello world!"
    }

}
