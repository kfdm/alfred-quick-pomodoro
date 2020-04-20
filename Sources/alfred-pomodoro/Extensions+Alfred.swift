//
//  Extensions+Alfred.swift
//
//  Created by Paul Traylor on 2020/04/19.
//

import Foundation

struct AlfredIcon: Codable {
    let path: String
}

struct AlfredRow: Codable {
    let arg: String
    let title: String
    let icon: AlfredIcon?
}

extension AlfredRow {
    init(title: String, date: Date, icon: AlfredIcon? = nil) {
        let formatter = DateFormatter()
        formatter.dateFormat = "yyyy-MM-dd"

        self.title = title
        self.arg = formatter.string(from: date)
        self.icon = icon
    }
}

struct AlfredJson: Codable {
    let items: [AlfredRow]
}

extension AlfredJson {
    var json: String {
        let jsonData = try! JSONEncoder().encode(self)
        return String(data: jsonData, encoding: .utf8)!
    }
}
