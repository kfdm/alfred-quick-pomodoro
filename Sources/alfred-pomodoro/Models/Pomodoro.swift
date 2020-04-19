//
//  Pomodoro.swift
//  NextPomodoro
//
//  Created by Paul Traylor on 2018/09/09.
//  Copyright © 2018年 Paul Traylor. All rights reserved.
//

import Foundation

struct Pomodoro: Codable {
    let id: Int
    var title: String
    var start: Date
    var end: Date
    var project: String?
    var memo: String?
}

typealias ResultSinglePomodoro = (Result<Pomodoro, Error>) -> Void

extension Pomodoro {
    init(title: String, project: String?, minutes: Int?) {
        id = 0
        self.title = title
        self.project = project
        start = Date()
        end = Date(timeIntervalSinceNow: TimeInterval((minutes ?? 25) * 60))
    }

    func submit(completionHandler handler: @escaping ResultSinglePomodoro) {
        URLSession.shared.authedRequest(path: "/api/pomodoro", method: .POST, body: toData(), completionHandler: { response in
            handler(response.map { (data) -> Pomodoro in
                Pomodoro.fromData(data)!
            })
        })
    }
}
