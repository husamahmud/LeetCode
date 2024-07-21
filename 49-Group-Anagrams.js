const sortStr = (str) => {
  return str.split('').sort().join('')
}

var groupAnagrams = function (strs) {
  const map = {}
  const result = []

  for (const str of strs) {
    let sortedStr = sortStr(str)

    if (map[sortedStr]) {
      map[sortedStr].push(str)
    } else {
      map[sortedStr] = [str]
    }
  }

  for (const [key, val] of Object.entries(map)) {
    result.push(val)
  }

  return result
};