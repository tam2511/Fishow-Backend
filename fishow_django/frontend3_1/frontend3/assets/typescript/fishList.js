'use strict'
exports.__esModule = true
const doFishObject = function (fishArray) {
  if (fishArray && fishArray.length === 0) {
    return null
  }
  const result = []
  fishArray.forEach(function (fish) {
    result.push({
      title: fish,
      image: '/fish_green/' + fish + '.jpg',
    })
  })
  return result
}
exports.default = doFishObject
