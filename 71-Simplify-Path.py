class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = ['/']
        full_path = path.split('/')

        for d in full_path:
            if d == '' or d == '.':
                continue
            elif d == '..' or d == '//':
                stack.pop()
                if stack:
                    stack.pop()
            else:
                stack.append(d)
                stack.append('/')
            if not stack:
                stack.append('/')
            print(stack)


        if len(stack) > 1 and stack[-1] == '/':
            stack.pop()
        if not stack:
            stack.append('/')

        print(stack)

        return \\.join(stack)