type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type Obj = Record<string, JSONValue> | Array<JSONValue>;

function chunk(arr: Obj[], size: number): Obj[] {
  const res: Obj[][] = []
  let currChunk: Obj[] = []
  let i: number

  for (i = 0; i < arr.length; i++) {
    currChunk.push(arr[i])

    if (currChunk.length === size) {
      res.push(currChunk)
      currChunk = []
    }
  }

  if (currChunk.length) res.push(currChunk)
  return res
};
