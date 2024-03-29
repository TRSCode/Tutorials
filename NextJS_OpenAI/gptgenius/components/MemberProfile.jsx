import { fetchOrGenerateTokens } from '@/utils/action';
import { UserButton, auth, currentUser } from '@clerk/nextjs';

const MemberProfile = async () => {
    const user = await currentUser();
    const { userId } = auth();
    // console.log(user);

    await fetchOrGenerateTokens(userId);

    return (
        <div className="fx-4 flex items-center gap-2">
            <UserButton afterSignOutUrl='/' />
            <p>
                {user.emailAddresses[0].emailAddress}
            </p>
        </div>
    )
}

export default MemberProfile