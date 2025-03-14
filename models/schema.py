import humanize
from app import db
from typing import List
from datetime import datetime, timedelta
from sqlalchemy import String, Integer, Text, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Users(db.Model):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(80), nullable=False)
    username: Mapped[str] = mapped_column(String(120), nullable=False)
    phone: Mapped[str] = mapped_column(String(17), nullable=False)
    email: Mapped[str] = mapped_column(String(80), nullable=False)
    photo: Mapped[str] = mapped_column(Text, nullable=True)
    password: Mapped[str] = mapped_column(String(140), nullable=False)

    user_post: Mapped[List["Posts"]] = relationship("Posts", back_populates="post", cascade="all, delete-orphan")
    user_reaction: Mapped[List["Reactions"]] = relationship("Reactions", back_populates="user")
    user_comment: Mapped[List["Comments"]] = relationship("Comments", back_populates="user")

    def __repr__(self):
        return f'User {self.name}, {self.email}'
    
class Comments(db.Model):
    __tablename__ = 'comment'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)
    post_id: Mapped[int] = mapped_column(ForeignKey('post.id'), nullable=False)

    user: Mapped["Users"] = relationship("Users", back_populates="user_comment")
    post: Mapped["Posts"] = relationship("Posts", back_populates="commented_post")

    def time_since_commented(self):
        return humanize.naturaltime(datetime.utcnow - self.created_at)
    
    def __repr__(self):
        return f'User {self.user_id} commented in post {self.post_id} since {self.time_since_commented()}'
    
class Posts(db.Model):
    __tablename__ = 'post'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    cover: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)

    post: Mapped["Users"] = relationship("Users", back_populates="user_post")
    commented_post: Mapped[List["Comments"]] = relationship("Comments", back_populates="post", cascade="all, delete-orphan")
    reacted_post: Mapped[List["Reactions"]] = relationship("Reactions", back_populates="post")

    def __repr__(self):
        return f'User {self.user_id} posted {self.title} at {self.created_at}'
    
class Reactions(db.Model):
    __tablename__ = 'reaction'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    react: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)

    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)
    post_id: Mapped[int] = mapped_column(ForeignKey('post.id'), nullable=False)

    user: Mapped["Users"] = relationship("Users", back_populates="user_reaction")
    post: Mapped["Posts"] = relationship("Posts", back_populates="reacted_post")

class TokenBlockList(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    jti: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime, nullable=False, server_default=db.func.now())