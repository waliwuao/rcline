# rcline 库新手教程

欢迎使用 rcline 库！这是一个用于 2D 猫和线互动模拟的 Python 库，包含碰撞检测功能。本教程将帮助你快速上手使用这个库创建简单的模拟场景。

## 目录
1. [安装与导入](#1-安装与导入)
2. [核心概念](#2-核心概念)
3. [快速开始](#3-快速开始)
4. [创建实体](#4-创建实体)
   - [创建猫(Cat)](#41-创建猫cat)
   - [创建线(Line)](#42-创建线line)
5. [创建地图(Map)](#5-创建地图map)
6. [运行模拟](#6-运行模拟)
7. [进阶操作](#7-进阶操作)
8. [示例代码](#8-示例代码)

## 1. 安装与导入

首先，确保你已经安装了 rcline 库。然后在代码中导入所需的类：
```bash
pip install rcline
```

```python
from rcline import Cat, Line, Map
```

## 2. 核心概念

rcline 库主要包含以下核心组件：

- **实体(Entity)**: 所有可在地图上显示的对象的基类
- **猫(Cat)**: 可移动的圆形实体，可以是可控的
- **线(Line)**: 直线实体，有普通线和实线两种（实线可碰撞）
- **地图(Map)**: 包含所有实体的场景，负责运行模拟
- **碰撞检测(Collide)**: 内置的碰撞检测系统，自动处理实体间的碰撞

## 3. 快速开始

让我们从一个简单的例子开始，创建一个包含一只可控猫和边界的地图：

```python
# 创建地图
sim_map = Map(width=20, height=15, title="我的第一个模拟")

# 创建一只可控的猫，初始位置在(10, 7)
cat = Cat(x=10, y=7, radius=0.5, controllable=True)

# 将猫添加到地图
sim_map.add_entity(cat)

# 开始模拟
sim_map.start_simulation()
```

运行这段代码，你将看到一个带网格的窗口，中间有一只猫，你可以使用方向键控制它移动，它会被地图边界阻挡。

## 4. 创建实体

### 4.1 创建猫(Cat)

`Cat` 类用于创建猫实体，常用参数：

- `x`, `y`: 初始位置坐标
- `radius`: 猫的半径（大小）
- `vx`, `vy`: 初始速度
- `controllable`: 是否可通过键盘控制（True/False）
- `color`: 颜色（默认为蓝色）
- `move_acceleration`: 加速度大小
- `friction`: 摩擦系数（影响减速效果）

示例：

```python
# 创建一只红色的猫，不可控，有初始速度
fast_cat = Cat(
    x=5, y=5, 
    radius=0.6,
    vx=2, vy=1,  # 初始速度
    color="#FF0000",  # 红色
    controllable=False
)
```

### 4.2 创建线(Line)

`Line` 类用于创建线实体，常用参数：

- `start_x`, `start_y`: 起点坐标
- `end_x`, `end_y`: 终点坐标
- `color`: 颜色
- `solid`: 是否为实线（True/False，实线可碰撞）

示例：

```python
# 创建一条实线（可碰撞）
solid_line = Line(
    start_x=3, start_y=3,
    end_x=10, end_y=3,
    solid=True  # 实线，猫会被阻挡
)

# 创建一条虚线（不可碰撞）
dashed_line = Line(
    start_x=3, start_y=5,
    end_x=10, end_y=5,
    solid=False  # 虚线，猫可以穿过
)
```

## 5. 创建地图(Map)

`Map` 类用于创建模拟场景，常用参数：

- `width`, `height`: 地图宽和高
- `title`: 模拟窗口标题
- `grid_step`: 网格间距

地图方法：

- `add_entity(entity)`: 添加实体到地图
- `remove_entity(entity)`: 从地图移除实体
- `start_simulation(interval)`: 开始模拟，interval 是帧间隔（毫秒）
- `stop_simulation()`: 停止模拟

示例：

```python
# 创建一个更大的地图
large_map = Map(
    width=30, 
    height=20, 
    title="大型模拟场景",
    grid_step=2  # 网格间距为2
)
```

## 6. 运行模拟

创建好地图和实体后，只需调用 `start_simulation()` 方法即可开始模拟：

```python
# 开始模拟，每50毫秒更新一帧
large_map.start_simulation(interval=50)
```

模拟窗口中：
- 对于可控猫，使用方向键（上、下、左、右）控制移动
- 关闭窗口即可停止模拟

## 7. 进阶操作

### 7.1 碰撞检测

rcline 库会自动处理碰撞检测：
- 猫与实线会发生碰撞
- 猫与猫之间会发生碰撞
- 实线与实线之间会发生碰撞检测

### 7.2 自定义颜色

你可以在创建实体时指定颜色，支持多种颜色格式：
- 命名颜色："red", "blue"
- 十六进制："#FF0000", "#3B82F6"
- RGB 元组：(1.0, 0.5, 0.0)

### 7.3 实体更新

每个实体都有 `update()` 方法，在模拟过程中会被定期调用。你可以继承 `Cat` 或 `Line` 类并重写此方法来实现自定义行为。

## 8. 示例代码

下面是一个完整的示例，创建一个包含多只猫和多条线的场景：

```python
from rcline import Cat, Line, Map

# 创建地图
sim_map = Map(width=25, height=20, title="猫和线的模拟")

# 创建几只猫
player_cat = Cat(
    x=5, y=10, 
    radius=0.6,
    controllable=True,
    color="#3B82F6",  # 蓝色
    move_acceleration=3
)

enemy_cat1 = Cat(
    x=15, y=5, 
    radius=0.5,
    vx=1, vy=0.5,
    color="#EF4444"   # 红色
)

enemy_cat2 = Cat(
    x=20, y=15, 
    radius=0.5,
    vx=-0.8, vy=-0.3,
    color="#EF4444"   # 红色
)

# 创建一些线
solid_line1 = Line(5, 7, 15, 7, solid=True)
solid_line2 = Line(15, 7, 15, 13, solid=True)
solid_line3 = Line(15, 13, 5, 13, solid=True)

dashed_line1 = Line(5, 9, 13, 9, solid=False)
dashed_line2 = Line(5, 11, 13, 11, solid=False)

# 添加所有实体到地图
sim_map.add_entity(player_cat)
sim_map.add_entity(enemy_cat1)
sim_map.add_entity(enemy_cat2)
sim_map.add_entity(solid_line1)
sim_map.add_entity(solid_line2)
sim_map.add_entity(solid_line3)
sim_map.add_entity(dashed_line1)
sim_map.add_entity(dashed_line2)

# 开始模拟
sim_map.start_simulation(interval=40)
```

运行这个示例，你将看到一个有边界的场景，里面有一只你可以控制的蓝色猫和两只自动移动的红色猫，还有一些实线（红色）和虚线（灰色），猫会与实线和其他猫发生碰撞。

---

希望这个教程能帮助你快速了解 rcline 库的基本使用方法。通过组合不同的实体和参数，你可以创建各种有趣的模拟场景！

