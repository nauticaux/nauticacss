import sass
import rcssmin

compile_array = [
    {"project/sass/main/base.scss": "dist/pinta.core.css"},
    {"project/sass/main/medium.scss": "dist/pinta.responsive-768.css"},
    {"project/sass/main/large.scss": "dist/pinta.responsive-1024.css"},
    {"project/sass/main/extra-large.scss": "dist/pinta.responsive-1280.css"},
    {"project/sass/main/responsive.scss": "dist/pinta.responsive.css"},
]

minify_array = [
    {"dist/pinta.core.css": "dist/pinta.core.min.css"},
    {"dist/pinta.responsive-768.css": "dist/pinta.responsive-768.min.css"},
    {"dist/pinta.responsive-1024.css": "dist/pinta.responsive-1024.min.css"},
    {"dist/pinta.responsive-1280.css": "dist/pinta.responsive-1280.min.css"},
    {"dist/pinta.responsive.css": "dist/pinta.responsive.min.css"},
    # {"project/css/global.css": "dist/pinta.global.min.css"},
    # {"project/css/elements.css": "dist/pinta.elements.min.css"},
    # {"project/responsive/mobilefirst.css": "dist/pinta.mobilefirst.min.css"}
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
