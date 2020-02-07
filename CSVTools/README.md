# Save your time while operating on CSV file!

There are some functions which will save your time while handling a CSV file.

| Function's name | Description |
| --------------- | --------------------------------------|
|[Transform](#Transform) | Turn the row into column.(The output now is text format) |

# Details

**CSVOperation.Transform(ReadName, StartRow, StartColumn, SaveName = '')**

*Turn the row into column.*

| Parameters' name | type | Description |
| ---------------- | ---- | ----------- |
| ReadName | string | Name of CSV file, without ".csv" |
| StartRow | int | Start row number |
| StartColumn | int | Start column number |
| SaveName | string | Name of output file, default: SaveName + "_transform.csv" |

##<T id="Transform"> Transform </T>

For example, we want to handle a CSV file named "test.csv": the area in the red box will be turned.

![image](pictures_for_README/transform_origin.png)

Code:

```
import CSVOperation

CSVOperation.Transform("test", 6, 4)
```

Here is the result:

![image](pictures_for_README/transform_after.png)