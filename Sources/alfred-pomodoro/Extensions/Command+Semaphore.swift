//
//  StartCommand.swift
//
//  Created by Paul Traylor on 2020/04/19.
//

import Foundation
import SwiftCLI

class SemaphoreCommand {
    let sema = DispatchSemaphore(value: 0)
    
    open func executeSemaphore() throws {}

    func execute() throws {
        try executeSemaphore()
        sema.wait()
    }
}
