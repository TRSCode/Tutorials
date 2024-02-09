import Link from 'next/link';
const url = 'https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i=';
import drinkImg from './drink.jpg';
console.log(drinkImg);
import Image from 'next/image';

const getSingleDrink = async (id) => {
    const res = await fetch(`${url}${id}`);
    if(!res.ok){
        throw new Error('Failed to fetch a drink...');
    }
    return res.json();
}

const SingleDrinkPage = async ({params}) => {
    const data = await getSingleDrink(params.id);
    // console.log(params)
    // console.log(data)
    const title = data?.drinks[0]?.strDrink
    const imgSrc = data?.drinks[0]?.strDrinkThumb
    console.log(title,imgSrc);
    return (
        // <div>SingleDrinkPage</div>
        <div>
            <Link href='/drinks' className="btn btn-primary mt-8 mb-12">
                back to drinks
            </Link>
            {/* <img src={drinkImg.src} /> */}
            {/* <Image src={drinkImg} className='w-48 h-48 rounded-lg' alt='drink' /> */}
            {/* to use a remote image, next.config needs to be modified */}
            <Image 
            src={imgSrc} 
            width={300} 
            height={300} 
            className='w-48 height-48 rounded-lg shadow-lg mb-4' 
            priority 
            alt={title}
            />
            <h1 className="text-4xl mb-8">{title}</h1>
        </div>
    )
}

export default SingleDrinkPage