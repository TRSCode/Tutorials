// export function middleware(){
//     // console.log('middleware');
//     return Response.json({msg: 'hello there'});
// }

// export const config = {
//     matcher:'/about',
// }

import { NextResponse } from 'next/server';

export function middleware(request) {
    // console.log('middleware');
    return NextResponse.redirect(new URL('/', request.url))
}

export const config = {
    // a list of matchers or a single matcher
    matcher:['/about/:path*'],
}