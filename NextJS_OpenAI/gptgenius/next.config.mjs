// /** @type {import('next').NextConfig} */
// const nextConfig = {};

// export default nextConfig;

// /** @type {import('next').NextConfig} */
// const nextConfig = {
//     images: {
//         remotePatterns: [
//             {
//                 protocol: 'https',
//                 hostname: 'oaidalleapiprodscus.blob.core.windows.net',
//                 port: '',
//                 pathname: '/private/**',
//             },
//             {
//                 protocol: 'https',
//                 hostname: 'images.unsplash.com',
//                 port: '',
//                 pathname: '/**',
//             },
//         ],
//     },
// };

// export default nextConfig;

// next.config.mjs

/** @type {import('next').NextConfig} */
const nextConfig = {
    images: {
        remotePatterns: [
            {
                protocol: 'https',
                hostname: 'oaidalleapiprodscus.blob.core.windows.net',
                port: '',
                pathname: '/private/**',
            },
            {
                protocol: 'https',
                hostname: 'images.unsplash.com',
                port: '',
                pathname: '/**',
            },
        ],
    },
};

export default nextConfig;
