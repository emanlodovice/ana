import path from 'path';

const STATIC_URL = process.env.STATIC_URL || 'http://localhost:5000/'
const NODE_ENV = process.env.NODE_ENV || 'production';

function resolvePath(staticPath) {
    return path.join(__dirname, 'static', staticPath);
}

const javascriptRegex = /\.jsx?$/;
const stylesheetsRegex = /\.scss$/;
const imagesRegex = /\.(jpe?g|png|gif|svg)$/;
const fontsRegex = /\.(ttf|otf|woff2?)$/;

export default {
    entry: resolvePath('ana/index.jsx'),

    output: {
        path: resolvePath('build/ana'),
        filename: 'index.js',
        chunkFilename: '[name].js',
        publicPath: STATIC_URL
    },

    mode: NODE_ENV === 'production' ? 'production' : 'development',

    module: {
        rules: [{
            test: javascriptRegex,
            loader: 'babel-loader'
        }, {
            test: stylesheetsRegex,
            use: ['style-loader', 'css-loader', 'sass-loader']
        }, {
            test: [imagesRegex, fontsRegex],
            loader: 'file-loader',
            options: {
                name: '[name].[ext]'
            }
        }]
    }
};
