import path from 'path';

const NODE_ENV = process.env.NODE_ENV || 'development';

function resolvePath(staticPath) {
    return path.join(__dirname, 'ana/static/ana', staticPath);
}

const javascriptRegex = /\.jsx?$/;
const stylesheetsRegex = /\.scss$/;
const imagesRegex = /\.(jpe?g|png|gif|svg)$/;
const fontsRegex = /\.(ttf|otf|woff2?)$/;

export default {
    entry: resolvePath('source/index.jsx'),

    output: {
        path: resolvePath('dist'),
        filename: 'index.js',
        chunkFilename: '[name].js'
    },

    mode: NODE_ENV === 'production' ? 'production' : 'development',

    module: {
        rules: [{
            test: javascriptRegex,
            loader: 'babel-loader'
        }, {
            test: stylesheetsRegex,
            use: [{
                loader: 'style-loader'
            }, {
                loader: 'css-loader',
                options: {
                    modules: true
                }
            }, {
                loader: 'sass-loader'
            }]
        }, {
            test: [imagesRegex, fontsRegex],
            loader: 'file-loader',
            options: {
                name: '[name].[ext]'
            }
        }]
    }
};
