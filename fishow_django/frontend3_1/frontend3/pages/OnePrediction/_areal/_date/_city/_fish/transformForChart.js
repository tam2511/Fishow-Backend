export default (data) => {
  if (!data) return
  const time = []
  const result = []

  data.forEach((item) => {
    result.push(item.prob)
    time.push(item.time)
  })

  return {
    prob: [...result],
    time: [...time],
  }
}
