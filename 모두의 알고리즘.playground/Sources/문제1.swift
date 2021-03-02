import Foundation

// 문제 1

public func sum_1toN(n: Int) -> Int {
    return (n * (n + 1)) / 2
}


// 연습문제 1-1

//public func sumPow_1toN(n: Int) -> Int {
//    var sum = 0
//    for i in 0...n {
//        sum += Int(pow(Double(i), 2.0))
//    }
//    return sum
//}

// 연습문제 1-2
// 답: O(n)

// 연습문제 1-3 : O(1)

public func sumPow_1toN(n: Int) -> Int {
    return (n * (n + 1) * ((2 * n) + 1)) / 6
}
