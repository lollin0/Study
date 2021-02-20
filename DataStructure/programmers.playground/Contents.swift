import UIKit

func solution(_ numbers:[Int]) -> String {
    var answer = ""
    var dic:[String: Int] = [:]
    var compare:[String: Int] = [:]
    for x in numbers {
        dic["\(x)"] = x
        compare["\(x)"] = x
    }
    for x in dic {
        if x.value >= 1000 {
            compare["\(x.key)"] = x.value / 1000
            continue
        }else if x.value >= 100 {
            compare["\(x.key)"] = x.value / 100
            continue
        }else if x.value >= 10 {
            compare["\(x.key)"] = x.value / 10
            continue
        }else {
            compare["\(x.key)"] = x.value
        }
    }
    
    for x in compare.sorted(by:>) {
        answer.append("\(dic[x.key]!)")

    }
    return answer
    
}

print(solution([3, 30, 34, 5, 9]))
