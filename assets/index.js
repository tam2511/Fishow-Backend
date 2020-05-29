const getData = (fromData,days) => {
    const returnData = (a, b) => {
        const predictDate = a.split('-')
        const someDate = new Date()
        const numberOfDaysToAdd = b
        someDate.setMonth(predictDate[1] - 1)
        someDate.setFullYear(predictDate[0])
        someDate.setDate(Number(predictDate[2])+ numberOfDaysToAdd)
        const dd = someDate.getDate()
        const mm = someDate.getMonth() + 1
        const newmm = mm.length > 1 ? mm : '0' + mm
        return dd + '/' + newmm
    }
    const result = []
    const iterator = (numberOfDays) => {
        for (let i = 0; i < numberOfDays; i++) {
            result.push(returnData(fromData,i))
        }
    }
    iterator(days)
    return result
}

// console.log(getData('2020-04-10', 10))

const data = '[3, 0, 2, 0, 0, 4, 6, 1, 5]'

const newResult = []

for (let i = 0; i < data.length; i++) {
    if (data[i].match(/[0-9]/)) {
        newResult.push(Number(data[i]))
    }
}

console.log('newResult = ', newResult)
