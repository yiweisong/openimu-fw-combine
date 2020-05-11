# How to use

The components list of a whole bin

```
- bootloader          start: 0x00000
- calibration         start: 0x08000
- configuration       start: 0x0c000
- app                 start: 0x10000
```

## Run

Default

```
python3 main.py
```

With parameter
```
python3 main.py --bootloader=xxx.path --calibration=yyy.path --configuration=zzz.path --app=sss.path
```