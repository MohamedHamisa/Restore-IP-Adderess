class Solution:
    def restoreIpAddresses(self, s: str):
        def is_valid(s):
            for x in s:
                if x.startswith('0') and len(x) > 1 or int(x) > 255:
                    return False
            return True
        ans = []
        for i in range(1,len(s)-2):
            for j in range(i+1, len(s) - 1):
                for k in range(j+1, len(s) ):
                    ip = [s[:i],s[i:j],s[j:k],s[k:]]
                    if is_valid(ip):
                        ans.append(".".join(ip))
        return ans





