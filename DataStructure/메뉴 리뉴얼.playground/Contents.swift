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
    print(combination(array: menu, int: 2))
    
    
    
    return answer
    
}

func combination(array: [Character], int: Int) -> [String]{
    var com:[String] = []*int
    for index in 0...int {
        for x in 0...array.count {
            com[index]
        }
    }
    for x in 0...array.count {
        for y in x...array.count-(x+1) {
            var currentCom = String(array[x]) + String(array[y+1])
            print(currentCom)
            com.append(currentCom)
        }
    }
    return com
}


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
