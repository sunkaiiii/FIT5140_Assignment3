//
//  PlaceDetailResponse.swift
//  FIT5140Assignment3iOS
//
//  Created by sunkai on 3/11/20.
//

import Foundation

// MARK: - PlaceDetailResponse
struct PlaceDetailResponse: Codable {
    let result: PlaceDetail
}

// MARK: - Result
struct PlaceDetail: Codable {
    
    let addressComponents: [AddressComponent]
    let formattedAddress: String
    let geometry: PlaceDetailGeometry
    let icon: String
    let name, placeID: String
    let types: [String]?

    enum CodingKeys: String, CodingKey {
        case addressComponents = "address_components"
        case formattedAddress = "formatted_address"
        case geometry, icon, name
        case placeID = "place_id"
        case types
    }
}

struct AddressComponent: Codable {
    let longName, shortName: String
    let types: [String]

    enum CodingKeys: String, CodingKey {
        case longName = "long_name"
        case shortName = "short_name"
        case types
    }
}

// MARK: - Geometry
struct PlaceDetailGeometry: Codable {
    let location: PlaceDetailLocation
    let viewport: PlaceDetailViewport
}

// MARK: - Location
struct PlaceDetailLocation: Codable {
    let lat, lng: Double
}

// MARK: - Viewport
struct PlaceDetailViewport: Codable {
    let northeast, southwest: PlaceDetailLocation
}
