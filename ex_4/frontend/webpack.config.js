const path = require('path'),
    MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
    entry: {
        bundle: path.resolve(__dirname, "./src/index.js")
    },
    output: {
        filename: './js/[name].js',
        path: path.resolve(__dirname, './static/dist')
    },
    devtool: 'source-map',
    resolve: {
        alias: {
            "@": path.resolve(__dirname, './src'),
            "@js": path.resolve(__dirname, './src/js'),
            "@scss": path.resolve(__dirname, './src/scss'),
            "@fonts": path.resolve(__dirname, './src/fonts'),
        },
        extensions: [".scss", ".sass", ".js", ".css"]
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: ["babel-loader"]
            },
            {
                test: /\.s[ac]ss$/i,
                use: [
                    MiniCssExtractPlugin.loader,
                    {
                        loader: "css-loader",
                        options: {
                            sourceMap: true
                        }
                    },
                    {
                        loader: "postcss-loader",
                        options: {
                            sourceMap: true
                        }
                    },
                    {
                        loader: "sass-loader",
                        options: {
                            sourceMap: true,
                            additionalData: `
                                @import "@scss/_variables.scss";
                                @import "@scss/_mixins.scss";
                            `
                        }
                    }
                ]
            }
        ]
    },
    plugins: [
        new MiniCssExtractPlugin({
            filename: "css/[name].css",
            chunkFilename: "[id].css"
        })
    ]
}