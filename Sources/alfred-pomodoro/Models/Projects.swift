//
//  Projects.swift
//  KeychainAccess
//
//  Created by Paul Traylor on 2020/04/19.
//

import Foundation

struct Project: Codable {
    let id: String
    let name: String
    let color: String
    // let url: URL?
    // let memo: String?

    struct List: Codable {
        let count: Int
        let next: String?
        let previous: String?
        let results: [Project]
    }
}

typealias ResultProjects = (Result<[Project], Error>) -> Void

extension Project {
    static func list(completionHandler handler: @escaping ResultProjects) {
        let sema = DispatchSemaphore(value: 0)
        
        URLSession.shared.authedRequest(path: "/api/project", method: .GET, completionHandler: { result in
            handler(result.map({ (data) -> [Project] in
                let favorites: Project.List = Project.List.fromData(data)!
                return favorites.results
            }))
        })
    }
}
