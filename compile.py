import sass
import rcssmin

compile_array = [
    {"project/core/base.scss": "dist/nautica.core.css"},
    {"project/core/responsive-768.scss": "dist/nautica.responsive-768.css"},
    {"project/core/responsive-1024.scss": "dist/nautica.responsive-1024.css"},
    {"project/core/responsive-1280.scss": "dist/nautica.responsive-1280.css"},
    {"project/theming/theming.scss": "dist/nautica.theming.css"},
    {"project/components/components.scss": "dist/nautica.components.css"},
]

minify_array = [
    {"dist/nautica.core.css": "dist/min/nautica.core.min.css"},
    {"dist/nautica.responsive-768.css": "dist/min/nautica.responsive-768.min.css"},
    {"dist/nautica.responsive-1024.css": "dist/min/nautica.responsive-1024.min.css"},
    {"dist/nautica.responsive-1280.css": "dist/min/nautica.responsive-1280.min.css"},
    {"dist/nautica.theming.css": "dist/min/nautica.theming.min.css"},
    {"dist/nautica.components.css": "dist/min/nautica.components.min.css"},
]

def compile_sass(sass_array):
    for file in sass_array:
        for source, dest in file.items():
            with open(dest, "w") as outfile:
                outfile.write(sass.compile(filename=source))
            print(f"{source} compiled to {dest}")


def minify_css(css_array):
    for file in css_array:
        for source, dest in file.items():
            with open(source, "r") as infile:
                with open(dest, "w") as outfile:
                    outfile.write(rcssmin.cssmin(infile.read()))
            print(f"{source} minified to {dest}")


if __name__ == '__main__':
    compile_sass(compile_array)
    minify_css(minify_array)
