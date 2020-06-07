const doFishObject = (fishArray: Array<string>) => {
  if (fishArray && fishArray.length === 0) {
    return null
  }
  const result: Array<object> = []
  fishArray.forEach((fish) => {
    result.push({
      title: fish,
      image: '/fish_green/' + fish + '.jpg',
    })
  })
  return result
}

export default doFishObject
