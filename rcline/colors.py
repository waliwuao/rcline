# rcline/colors.py
from matplotlib.colors import LinearSegmentedColormap

PRIMARY_COLOR = '#3B82F6'
SECONDARY_COLOR = '#10B981'
ACCENT_COLOR = '#EF4444'
LIGHT_GRAY = '#F8FAFC'
MEDIUM_GRAY = '#E2E8F0'
DARK_GRAY = '#334155'
BACKGROUND_COLOR = '#FFFFFF'
GRID_MAJOR_COLOR = '#E2E8F0'
GRID_MINOR_COLOR = '#F1F5F9'

SIMPLE_CMAP = LinearSegmentedColormap.from_list(
    'simple_cmap', [PRIMARY_COLOR, SECONDARY_COLOR]
)

ENTITY_COLORS = {
    'cat': PRIMARY_COLOR,
    'line': DARK_GRAY,
    'solid_line': ACCENT_COLOR
}