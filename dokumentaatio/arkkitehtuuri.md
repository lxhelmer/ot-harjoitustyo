```mermaid
classDiagram
    tableHandler "*" -- "1" handlerManager
    privilegeHandler "1" -- "1" handlerManager
    class tableHandler{
        table actions
        table(sql)
    }
    class handlerManager{
        tableHandlers(list)
        ui
    }
    class privilegeHandler{
        privilegTier(int)
        manager
    }
```
