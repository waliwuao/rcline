# rcline 库新手教程

欢迎使用 rcline 库！这是一个用于 2D 猫和线互动模拟的 Python 库，包含碰撞检测功能。本教程将帮助你快速上手使用这个库创建简单的模拟场景。

## 目录
1. [安装与导入](#1-安装与导入)
2. [核心概念](#2-核心概念)
3. [快速开始](#3-快速开始)
4. [创建实体](#4-创建实体)
   - [创建猫(Cat)](#41-创建猫cat)
   - [创建线(Line)](#42-创建线line)
   - [创建多边形(Polygon)](#43-创建多边形polygon)
   - [创建圆形(Circle)](#44-创建圆形circle)
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
from rcline import Cat, Line, Polygon, Circle, Map
```

## 2. 核心概念

rcline 库主要包含以下核心组件：

- **实体(Entity)**: 所有可在地图上显示的对象的基类
- **猫(Cat)**: 可移动的圆形实体，可以是可控的
- **线(Line)**: 直线实体，有普通线和实线两种（实线可碰撞）
- **多边形(Polygon)**: 由多条线段组成的闭合或开放图形，支持碰撞检测
- **圆形(Circle)**: 圆形线条实体，可设置为实线（可碰撞）或普通线
- **地图(Map)**: 包含所有实体的场景，负责运行模拟
- **碰撞检测(Collide)**: 内置的碰撞检测系统，自动处理实体间的碰撞

## 3. 快速开始

让我们从一个简单的例子开始，创建一个包含一只可控猫和边界的地图：

```python
# 创建地图
sim_map = Map(width=20, height=15, title="我的第一个模拟")

# 创建一只可控的猫，初始位置在(10, 7)
cat = Cat(point=(10, 7), radius=0.5, controllable=True)

# 将猫添加到地图
sim_map.add_entity(cat)

# 开始模拟
sim_map.start_simulation()
```

运行这段代码，你将看到一个带网格的窗口，中间有一只猫，你可以使用方向键控制它移动，它会被地图边界阻挡。

## 4. 创建实体

### 4.1 创建猫(Cat)

`Cat` 类用于创建猫实体，常用参数：

- `point`: 初始位置坐标元组 (x, y)
- `radius`: 猫的半径（大小）
- `vx`, `vy`: 初始速度
- `ax`, `ay`: 初始加速度
- `controllable`: 是否可通过键盘控制（True/False）
- `color`: 颜色（默认为蓝色）
- `move_acceleration`: 加速度大小
- `friction`: 摩擦系数（影响减速效果）

示例：

```python
# 创建一只红色的猫，不可控，有初始速度
fast_cat = Cat(
    point=(5, 5), 
    radius=0.6,
    vx=2, vy=1,  # 初始速度
    color="#FF0000",  # 红色
    controllable=False
)
```

### 4.2 创建线(Line)

`Line` 类用于创建线实体，常用参数：

- `points`: 线的端点坐标列表 [(x1, y1), (x2, y2)]
- `color`: 颜色
- `solid`: 是否为实线（True/False，实线可碰撞）

示例：

```python
# 创建一条实线（可碰撞）
solid_line = Line(
    points=[(3, 3), (10, 3)],
    solid=True  # 实线，猫会被阻挡
)

# 创建一条虚线（不可碰撞）
dashed_line = Line(
    points=[(3, 5), (10, 5)],
    solid=False  # 虚线，猫可以穿过
)
```

### 4.3 创建多边形(Polygon)

`Polygon` 类用于创建多边形实体，由多个点连接形成，常用参数：

- `points`: 点坐标列表，格式为 [(x1,y1), (x2,y2), ..., (xn,yn)]
- `color`: 颜色
- `solid`: 是否为实线（True/False，实线可碰撞）
- `close`: 是否闭合多边形（True/False）

示例：

```python
# 创建一个三角形实线多边形（可碰撞）
triangle = Polygon(
    points=[(5,5), (10,5), (7.5,10)],
    solid=True,
    close=True  # 闭合多边形
)

# 创建一个开放的虚线多边形（不可碰撞）
open_poly = Polygon(
    points=[(2,2), (4,6), (6,3), (8,7)],
    solid=False,
    close=False  # 不闭合
)
```

### 4.4 创建圆形(Circle)

`Circle` 类用于创建圆形线条实体，常用参数：

- `point`: 圆心坐标元组 (x, y)
- `radius`: 半径
- `color`: 颜色
- `solid`: 是否为实线（True/False，实线可碰撞）

示例：

```python
# 创建一个实线圆形障碍物（可碰撞）
solid_circle = Circle(
    point=(10, 10),
    radius=2,
    solid=True
)

# 创建一个虚线圆形标记（不可碰撞）
dashed_circle = Circle(
    point=(15, 8),
    radius=3,
    solid=False
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

rcline 库会自动处理多种碰撞检测：
- 猫与实线/实线多边形/实线圆形会发生碰撞
- 猫与猫之间会发生碰撞
- 线与线之间会发生碰撞检测
- 圆形与线/圆形之间会发生碰撞检测

当猫发生碰撞时，会呈现脉冲动画效果（外圈短暂扩大），提示碰撞发生。非可控猫在碰撞时会自动反弹，遵循物理反射规律。

### 7.2 自定义颜色

你可以在创建实体时指定颜色，支持多种颜色格式：
- 命名颜色："red", "blue"
- 十六进制："#FF0000", "#3B82F6"
- RGB 元组：(1.0, 0.5, 0.0)

库中还提供了预设颜色常量，可直接使用：
```python
from rcline import PRIMARY_COLOR, SECONDARY_COLOR, ACCENT_COLOR, ENTITY_COLORS
```

其中 `ENTITY_COLORS` 包含了实体的默认颜色定义：
- `ENTITY_COLORS['cat']`: 猫的默认颜色（蓝色）
- `ENTITY_COLORS['line']`: 普通线的默认颜色（深灰色）
- `ENTITY_COLORS['solid_line']`: 实线的默认颜色（红色）

### 7.3 实体更新与自定义行为

每个实体都有 `update()` 方法，在模拟过程中会被定期调用。你可以继承 `Cat`、`Line`、`Polygon` 或 `Circle` 类并重写此方法来实现自定义行为。

例如：
- 重写 `Cat` 类的 `_handle_keyboard()` 方法可以改变控制方式
- 重写 `update()` 方法可以实现自动寻路、追踪目标等高级功能
- 重写 `draw()` 方法可以改变实体的外观

### 7.4 实体交互细节

- **猫的速度与摩擦**：猫的移动受加速度和摩擦系数影响，摩擦系数越大，减速越快
- **线的绘制细节**：实线会有轻微的黑色阴影效果，提高视觉辨识度
- **多边形的构成**：多边形由多条线段自动组成，闭合多边形会自动连接首尾点
- **碰撞反馈**：碰撞时猫会显示白色外圈脉冲效果，增强交互感知

## 8. 示例代码

下面是一个完整的示例，创建一个包含多只猫、线、多边形和圆形的场景：

```python
from rcline import Cat, Line, Polygon, Circle, Map

# 创建地图
sim_map = Map(width=25, height=20, title="猫和几何图形的模拟")

# 创建几只猫
player_cat = Cat(
    point=(5, 10), 
    radius=0.6,
    controllable=True,
    color="#3B82F6",  # 蓝色
    move_acceleration=3
)

enemy_cat1 = Cat(
    point=(15, 5), 
    radius=0.5,
    vx=1, vy=0.5,
    color="#EF4444"   # 红色
)

enemy_cat2 = Cat(
    point=(20, 15), 
    radius=0.5,
    vx=-0.8, vy=-0.3,
    color="#EF4444"   # 红色
)

# 创建一些线
solid_line1 = Line(points=[(5, 7), (15, 7)], solid=True)
solid_line2 = Line(points=[(15, 7), (15, 13)], solid=True)

# 创建一个多边形
hexagon = Polygon(
    points=[(10,10), (12,10), (13,12), (12,14), (10,14), (9,12)],
    solid=True,
    close=True
)

# 创建一个圆形障碍物
solid_circle = Circle(
    point=(18, 10),
    radius=1.5,
    solid=True
)

# 添加所有实体到地图
sim_map.add_entity(player_cat)
sim_map.add_entity(enemy_cat1)
sim_map.add_entity(enemy_cat2)
sim_map.add_entity(solid_line1)
sim_map.add_entity(solid_line2)
sim_map.add_entity(hexagon)
sim_map.add_entity(solid_circle)

# 开始模拟
sim_map.start_simulation(interval=40)
```

运行这个示例，你将看到一个包含多种几何形状的场景，可控的蓝色猫会与实线、多边形和圆形障碍物发生碰撞，并在碰撞时显示脉冲效果，红色猫会自动移动并在碰撞时反弹。

---

希望这个教程能帮助你快速了解 rcline 库的基本使用方法。通过组合不同的实体和参数，你可以创建各种有趣的模拟场景！