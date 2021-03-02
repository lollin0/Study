import UIKit
import Foundation

func solution(_ orders:[String], _ course:[Int]) -> [String] {
    var answer:[String] = []
    var menu:[Character] = []
    
    for x in orders {
        for y in x {
            menu.append(y)
        }
    }
    let removedDuplicate: Set = Set(menu)
    menu = Array(removedDuplicate) // 중복된 메뉴 제거
    menu = menu.sorted { $0 < $1 }
    for x in course {
        var com = combos(elements:menu, k:x)
        for x in 0..<com.count{
            for y in 0..<com[x].count{
                if com[x][y] == com[x][y+1] {
                    com.remove(at: x)
                }
            }
        }
        print("com: ", com)
    }
    
    return answer
    
}
func combos<T>(elements: ArraySlice<T>, k: Int) -> [[T]] {
    if k == 0 {
        return [[]]
    }

    guard let first = elements.first else {
        return []
    }

    let head = [first]
    let subcombos = combos(elements: elements, k: k - 1)
    var ret = subcombos.map { head + $0 }
    ret += combos(elements: elements.dropFirst(), k: k)
    
    
    return ret
}

func combos<T>(elements: Array<T>, k: Int) -> [[T]] {
    return combos(elements: ArraySlice(elements), k: k)
}

let numbers = [1,2,3,4,5]
//func combination(array: [Character], int: Int) -> [String]{
//    var com:[String] = []
//    for index in 0...int {
//        for x in 0...array.count {
//            com[index]
//        }
//    }
//    for x in 0...array.count {
//        for y in x...array.count-(x+1) {
//            var currentCom = String(array[x]) + String(array[y+1])
//            print(currentCom)
//            com.append(currentCom)
//        }
//    }
//    return com
//}


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
