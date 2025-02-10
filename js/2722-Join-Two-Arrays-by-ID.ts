type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type ArrayType = { "id": number } & Record<string, JSONValue>;

function join(arr1: ArrayType[], arr2: ArrayType[]): ArrayType[] {
  const obj = {}

  arr1.concat(arr2).forEach(item => {
    if (obj[item.id]) Object.assign(obj[item.id], item)
    else obj[item.id] = item
  })

  return Object.values(obj)
};

/* 
{"id": 1, "x": 2, "y": 3},
{"id": 2, "x": 3, "y": 6}

{"id": 2, "x": 10, "y": 20},
{"id": 3, "x": 0, "y": 0}

{"id": 1, "x": 2, "y": 3},
{"id": 2, "x": 10, "y": 20},
{"id": 3, "x": 0, "y": 0}
*/

/*
{"id": 1, "b": {"b": 94},"v": [4, 3], "y": 48}

{"id": 1, "b": {"c": 84}, "v": [1, 3]}

{"id": 1, "b": {"c": 84}, "v": [1, 3], "y": 48}
*/