class Target:
    def request(self) -> str:
        return "Target: The default target's behavior"
    

class Adaptee:
    def specific_request(self) -> str:
        return "this feature is specific behavior"
    

class Adapter(Target, Adaptee):
    """
    The Adapter makes the Adaptee's interface compatible with the Target's
    interface via multiple inheritance.
    """
    def request(self) -> str:
        print(super().request())
        return f"Adapter: (Translated) {self.specific_request()}"
    

if __name__=="__main__":
    print("Client: using jsut target object")
    target = Target()
    print(target.request())
    
    print("\n")
    
    # client use adapter
    adapter = Adapter()
    print(adapter.request())
    
    
    