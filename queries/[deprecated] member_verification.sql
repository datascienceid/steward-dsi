select users.username, 
    users_media.telegram, 
    users.created_at,
    idx_city.name city
from users
left join users_media on users.id = users_media.id_users
left join users_profile on users.id = users_profile.id_users
left join idx_city on idx_city.idx_city_id = users_profile.idx_city_id
where users_media.telegram = "<DISCORD_ID>"
group by 1,2,3,4;